using System;
using System.Collections;
using Server.Items;
using Server.Targeting;

namespace Server.Mobiles
{
	[CorpseName( "a wizard's body" )]
	public class RedWizard : BaseCreature
	{
		public override bool ShowFameTitle{ get{ return false; } }
		
		[Constructable]
		public RedWizard() : base( AIType.AI_Mage, FightMode.Closest, 10, 1, 0.2, 0.4 )

		{			
			SpeechHue = Utility.RandomDyedHue(); 
			Name = "a red wizard"; 
			Hue = Utility.RandomSkinHue(); 
			Body = 0x190; 

 	   		 // *Begin* //
   	   		Item gmrobe = new GMRobe();
      
         		gmrobe.Hue = 2118;
        		 gmrobe.Movable = false;

        		 AddItem( gmrobe );
        		 // *End* //
         
			SetStr( 75, 80 );
			SetDex( 90, 105 );
			SetInt( 160, 200 );
			SetHits( 150, 190 );

			SetDamage( 11, 15 );

			SetSkill( SkillName.MagicResist, 90.0, 100.0 );
			SetSkill( SkillName.EvalInt, 95.0, 100.0 );
			SetSkill( SkillName.Magery, 105.0, 110.0 );
			SetSkill( SkillName.Wrestling, 75.0, 80.0 );
			SetSkill( SkillName.Anatomy, 75.0, 80.0 );

			Fame = 7500;
			Karma = -625;

			VirtualArmor = 40;

			Item hair = new Item( Utility.RandomList( 0x203B, 0x2049, 0x2048, 0x204A ) );
			hair.Hue = Utility.RandomNondyedHue();
			hair.Layer = Layer.Hair;
			hair.Movable = false;
			AddItem( hair );

			

		}
	
		public override void GenerateLoot()
		{
			AddLoot( LootPack.Rich );
			AddLoot( LootPack.LowScrolls );
		}

		public override bool AlwaysMurderer{ get{ return true; } }

		public RedWizard( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version
		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();
		}
	}
}
