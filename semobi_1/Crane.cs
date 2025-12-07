using System;
using Server.Items;
using Server.Mobiles;

namespace Server.Mobiles
{
	[CorpseName( "a Crane corpse" )]
	public class Crane : BaseCreature
	{
		[Constructable]
		public Crane() : base( AIType.AI_Melee, FightMode.Closest, 10, 1, 0.2, 0.4 )
		{
			Name = "a Crane";
			Body = 254;
			BaseSoundID = 0x2EE;

			SetStr( 25, 35 );
			SetDex( 15, 25 );
			SetInt( 10, 15 );

			SetHits( 25, 35 );
			SetMana( 0, 0 );
			SetStam( 15, 25 );

			SetDamage( 1, 1 );

			SetDamageType( ResistanceType.Physical, 100 );

			SetResistance( ResistanceType.Physical, 5, 5 );

			SetSkill( SkillName.MagicResist, 4.0, 5.0 );
			SetSkill( SkillName.Tactics, 10.0, 11.0 );
			SetSkill( SkillName.Wrestling, 10.0, 11.0 );
			SetSkill( SkillName.Anatomy, 5.0, 6.0 );


			Fame = 15;
			Karma = 0;
			
			Tamable = false;
		}
		public override int Meat{ get{ return 1; } }
		public override MeatType MeatType{ get{ return MeatType.Bird; } }
		public override int Feathers{ get{ return 25; } }
		public override FoodType FavoriteFood{ get{ return FoodType.Fish; } }

                public Crane( Serial serial ) : base( serial )
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